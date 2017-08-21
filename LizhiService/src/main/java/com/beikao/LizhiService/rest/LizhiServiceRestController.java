package com.beikao.LizhiService.rest;

import com.beikao.LizhiService.domain.BroadcastItem;
import com.beikao.LizhiService.service.BroadcastService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class LizhiServiceRestController {
    @Autowired
    private BroadcastService service;

    private static Logger logger = LoggerFactory.getLogger(LizhiServiceRestController.class);

    @RequestMapping(value = "/broadcasts",method = RequestMethod.GET)
    public List<BroadcastItem> findAll() {
        return service.findAll();
    }

    @RequestMapping(value = "/crawler",method = RequestMethod.GET)
    public void crawlLizhiPages() {
        service.crawl();
    }

}
