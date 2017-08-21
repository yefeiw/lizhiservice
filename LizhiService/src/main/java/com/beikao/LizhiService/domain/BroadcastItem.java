package com.beikao.LizhiService.domain;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.io.Serializable;
import java.util.List;
@JsonInclude
@Data
@Document
public class BroadcastItem implements Serializable{
    private static final long serialVersionUID = 1L;

    @Id
    //ID of this broadcast
    public int id;
    //Title of this broadcast
    public String title;
    //Full text of this broadcast
    public String desc;
    //Host of the broadcast
    public String category;
    //List of Hosts
    public List<String> hosts;
    //Views
    public int numViews;

   @JsonCreator
   public BroadcastItem(@JsonProperty("id")int id,
                        @JsonProperty("title")String title,
                        @JsonProperty("desc")String desc,
                        @JsonProperty("category")String category,
                        @JsonProperty("hosts")List<String> hosts) {
       this.id = id;
       this.title = title;
       this.desc = desc;
       this.category = category;
       this.hosts = hosts;
   }

}
