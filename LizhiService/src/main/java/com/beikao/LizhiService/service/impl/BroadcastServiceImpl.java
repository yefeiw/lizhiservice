package com.beikao.LizhiService.service.impl;

import com.beikao.LizhiService.domain.*;
import com.beikao.LizhiService.service.BroadcastService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
//                    Host host = hostRepository.findByHostName(hostName);
//                    if (host == null) {
//                        int index = 0;
//                        for (index = 0; index < Crawler.hosts.length; index++) {
//                            if (Crawler.hosts[index].equals(hostName)) break;
//                        }
//                        if (index >= Crawler.hosts.length) {
//                            logger.warn("Host name " + hostName + "not found, discarding");
//                            continue;
//                        }
//                        host = new Host(String.valueOf(index), hostName);
//                    }
//                    host.addItem(item);
//                    hostRepository.save(host);
//                }
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
