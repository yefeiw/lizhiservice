package com.beikao.LizhiService.service.impl;

import com.beikao.LizhiService.domain.*;
import com.beikao.LizhiService.service.BroadcastService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service

public class BroadcastServiceImpl implements BroadcastService {
    @Autowired
    private BroadcastItemRepository broadcastItemRepository;

    private Crawler crawler = new Crawler();

    @Autowired
    private HostRepository hostRepository;

    private static Logger logger = LoggerFactory.getLogger(BroadcastServiceImpl.class);

        //Get all broadcastItems By each category
    @Override
    public List<BroadcastItem> findAllByCategory(String category) {
        return broadcastItemRepository.findAllByCategory(category);
    }
    //Get all broadcastItems by each host
    @Override
    public List<BroadcastItem> findAllByHostName(String name) {
        Host host = hostRepository.findByHostName(name);
        return host.getItems();
    }
    //Save broadcast item to repo
    @Override
    public BroadcastItem saveItem(BroadcastItem item) {
        return this.broadcastItemRepository.save(item);
    }
    //Save broadcast item to host
    @Override
    public Host saveHost(String name, BroadcastItem item) {
        Host host = hostRepository.findByHostName(name);
        if (host == null) {
            host = new Host(name);
        }
        host.addItem(item);
        return hostRepository.save(host);
    }
    @Override
    public List<BroadcastItem> findAll() {
        return broadcastItemRepository.findAll();
    }
    @Override
    public void crawl() {
        List<BroadcastItem> items = crawler.getLizhiItems();
    }
}
