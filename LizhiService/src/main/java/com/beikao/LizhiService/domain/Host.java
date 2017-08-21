package com.beikao.LizhiService.domain;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.repository.query.Param;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
@JsonInclude
@Data
@Document
public class Host implements Serializable {
    private static final long serialVersionUID = 2L;
    //Name of the category
    private String hostName;
    //List of Lizhi URLs that actually mapped to this host.
    private List<BroadcastItem> items;
    @JsonCreator
    public Host(@Param("name")String name) {

        this.hostName = name;
        this.items= new ArrayList<>();
    }
    //Add the designated URL into the list of URLs for this host.
    public void addItem(BroadcastItem item) {
        this.items.add(item);
    }
}
