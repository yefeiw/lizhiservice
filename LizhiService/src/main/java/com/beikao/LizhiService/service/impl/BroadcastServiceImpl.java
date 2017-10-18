package com.beikao.LizhiService.service.impl;

import com.beikao.LizhiService.domain.*;
import com.beikao.LizhiService.service.BroadcastService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import java.util.*;

@Service

public class BroadcastServiceImpl implements BroadcastService {
    @Autowired
    private BroadcastItemRepository broadcastItemRepository;

    private Crawler crawler = new Crawler();

    //TODO: make it a real mongoDB library so that it could scale
    Map<String, List<BroadcastItem>> hostStats = new HashMap<>();
    private static Logger logger = LoggerFactory.getLogger(BroadcastServiceImpl.class);

        //Get all broadcastItems By each category
    @Override
    public List<BroadcastItem> findAllByCategory(String category) {
        return broadcastItemRepository.findAllByCategory(category);
    }
    //Get all broadcastItems by each host
    @Override
    public List<BroadcastItem> findAllByHostName(String name) {
       // Host host = hostRepository.findByHostName(name);
        //return host.getItems();
        return hostStats.get(name);
    }
    //Save broadcast item to repo
    @Override
    public BroadcastItem saveItem(BroadcastItem item) {
        return this.broadcastItemRepository.save(item);
    }
    @Override
    public List<BroadcastItem> findAll() {
        return broadcastItemRepository.findAll();
    }
    @Override
    public void crawl() {
        List<BroadcastItem> items = crawler.getLizhiItems();
        try {
            for (BroadcastItem item : items) {
                broadcastItemRepository.save(item);
                List<String> hosts = item.getHosts();
                for (String hostName : hosts) {
                    if (!hostStats.containsKey(hostName)) {
                        hostStats.put(hostName,new ArrayList<>());
                    }
                    List<BroadcastItem> hostList = hostStats.get(hostName);
                    hostList.add(item);
                    hostStats.put(hostName,hostList);
                }
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
    @Override
    public void sendEmail() {
        try {
            generateAndSendEmail();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    private void generateAndSendEmail() throws AddressException, MessagingException {

        // Step1
        Properties mailServerProperties = System.getProperties();
        mailServerProperties.put("mail.smtp.port", "587");
        mailServerProperties.put("mail.smtp.auth", "true");
        mailServerProperties.put("mail.smtp.starttls.enable", "true");

        // Step2
        Session getMailSession = Session.getDefaultInstance(mailServerProperties, null);
        MimeMessage generateMailMessage = new MimeMessage(getMailSession);
        generateMailMessage.addRecipient(Message.RecipientType.TO, new InternetAddress("jeffxanthus@gmail.com"));
        generateMailMessage.setSubject("Discounts!");
        String emailBody = "Hi Dear Teammates" +
                "<br><br>Here are the latest updates of our statistics</br>";
       //TODO: add email body for each member.
        emailBody += "<br> Regards, <br>Yefei Wang";
        generateMailMessage.setContent(emailBody, "text/html");

        // Step3
        System.out.println("\n\n Get Session and Send mail");
        Transport transport = getMailSession.getTransport("smtp");

        // Enter your correct gmail UserID and Password
        // if you have 2FA enabled then provide App Specific Password
        transport.connect("smtp.gmail.com", "jeffxanthus@gmail.com", "AT900-Technique");
        transport.sendMessage(generateMailMessage, generateMailMessage.getAllRecipients());
        System.out.println("Email sent successfully");
        transport.close();
    }
}
