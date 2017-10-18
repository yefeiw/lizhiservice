package com.beikao.LizhiService.domain;

import java.util.ArrayList;
import java.util.List;

public class HostName {
    public static final String[] hosts = {
            "Ada",
            "丫头",
            "Ruby",
            "豆包",
            "老王",
            "黑人",
            "小哈",
            "奔奔",
            "九月",
            "波波",
            "大白"
    };
    public static final String[] hostEncodings = {
            "ada",
            "yatou",
            "ruby",
            "doubao",
            "laowang",
            "heiren",
            "xiaoha",
            "benben",
            "jiuyue",
            "bobo",
            "dabai"
    };
    public static List<String> getHosts(String hostText) {
        List<String> ret = new ArrayList<>();
        for (int i = 0; i < hosts.length; i++) {
            if (hostText.indexOf(hosts[i])!= -1) {
                ret.add(hostEncodings[i]);
            }
        }
        return ret;
    }
}
