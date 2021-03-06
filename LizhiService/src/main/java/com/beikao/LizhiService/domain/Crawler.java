package com.beikao.LizhiService.domain;
import com.beikao.LizhiService.service.BroadcastService;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.net.Authenticator;
import java.net.PasswordAuthentication;
import java.net.SocketException;
import java.net.SocketTimeoutException;
import java.util.*;
import java.util.logging.Logger;

import static com.beikao.LizhiService.domain.HostName.getHosts;
import static com.beikao.LizhiService.domain.HostName.hosts;

public class Crawler {
    //String constants
    private static final String USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36";
    //
    private final String authUser = "bittiger";
    private final String authPassword = "cs504";
    private final String LIZHI_HOME_URL = "http://lizhi.fm/40624/p/";

    private static final Logger logger = Logger.getLogger("crawler");


    public void initProxy() {

        System.setProperty("http.proxyHost", "199.101.97.178"); // set proxy server
        System.setProperty("http.proxyPort", "60099"); // set proxy port
        Authenticator.setDefault(
                new Authenticator() {
                    @Override
                    public PasswordAuthentication getPasswordAuthentication() {
                        return new PasswordAuthentication(
                                authUser, authPassword.toCharArray());
                    }
                }
        );
    }

    private String getCategory(String text) {
        if (text.indexOf("嘉宾")!= -1) {
            return "嘉宾";
        } else if (text.indexOf("吐槽") != -1) {
            return "吐槽";
        } else if (text.indexOf("互撕")!= -1) {
            return "互撕";
        } else if (text.indexOf("北美") != -1 || text.indexOf("在美国") != -1) {
            return "北美";
        } else {
            return "其他";
        }
    }




    public List<BroadcastItem> getLizhiItems() {
        HashSet<String> itemSet = new HashSet<>();
        List<BroadcastItem> ret = new ArrayList<>();

        try {
            HashMap<String, String> headers = new HashMap<String, String>();
            headers.put("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8");
            headers.put("Accept-Encoding", "gzip, deflate");
            headers.put("Accept-Language", "en-US,en;q=0.8");
            initProxy();
            boolean hasNextPage = true;
            int pageNum = 1;
            int programID = 1;
            while(hasNextPage) {
                String url = LIZHI_HOME_URL+pageNum+".html";
                Document doc;
                try {
                    doc = Jsoup.connect(url).maxBodySize(0).headers(headers).userAgent(USER_AGENT).timeout(3000).get();
                    Thread.sleep(500);
                } catch (Exception e) {
                    //try it again no matter what exception is reported.
                    logger.warning("timeout occurs, trying again");
                    continue;
                }
                logger.info("doc size is "+doc.body().text().length());
                Element castList = doc.getElementsByClass("js-audio-list").first();
                Elements casts =  castList.getElementsByClass("audio-list-item");
                for (int i = 0; i < casts.size();i++) {
                    Element cast = casts.get(i);
                    String title = cast.attr("title");
                    String href = "http://lizhi.fm"+cast.attr("href");
                    //Logging
                    logger.info("title is "+ title);
                    logger.info("href is "+href);
                    int id = programID++;
                    Document details;
                    try {
                        details = Jsoup.connect(href).maxBodySize(0).headers(headers).userAgent(USER_AGENT).timeout(3000).get();
                    } catch (Exception e) {
                        //No matter what exception is reported, should try it again.
                        i--;
                        programID--;
                        continue;
                    }
                    String text = details.getElementsByClass("desText").first().text();
//                    logger.info("text is "+text);
                    String keyword = "本期主播";
                    String hostRegion = "";
                    List<String> hosts = new ArrayList<>();
                    try {
                            int hostIndex = -1;
                            while(hosts.isEmpty()) {
                                hostIndex = text.indexOf(keyword,hostIndex+1);
                                hostRegion = text.substring(hostIndex, Math.min(hostIndex + 30, text.length() -1));
                                hosts = getHosts(hostRegion);
                            }

                        logger.info("Host search region is" + hostRegion);
                    } catch (Exception e) {
                        //fallback: search from full text
                        hosts = getHosts(text);
                        if (hosts.isEmpty()) {
                            logger.warning("No hosts for ref"+href);
                            //This is a bad link
                            continue;
                        }


                    }
                    logger.info("Host is "+ hosts);
                    logger.info("Category is "+getCategory(text));
                    String date = details.getElementsByClass("audioTime").text();
                    BroadcastItem item = new BroadcastItem(String.valueOf(id),title,text,getCategory(text),hosts);
                    item.setDate(date);
                    ret.add(item);
                }
                if(doc.getElementsByClass("next").size() > 0) {
                    pageNum++;
                    //TODO: comment it out in production code, enable it for testing purposes;
                    //hasNextPage =false;
                } else {
                    hasNextPage = false;
                }

            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return ret;
    }



}
