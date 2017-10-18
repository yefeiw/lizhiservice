package com.beikao.LizhiService.service;

import com.beikao.LizhiService.domain.BroadcastItem;
import com.beikao.LizhiService.domain.Host;

import java.util.List;

public interface BroadcastService {
    //Get all broadcastItems By each category
    List<BroadcastItem> findAllByCategory(String category);
    //Get all broadcastItems by each host
    List<BroadcastItem> findAllByHostName(String name);
    //Save broadcast item to repo
    BroadcastItem saveItem(BroadcastItem item);
    //Find all broadcasts
    List<BroadcastItem> findAll();
    //Crawl all related broadcasts and update record
    void crawl();
}
