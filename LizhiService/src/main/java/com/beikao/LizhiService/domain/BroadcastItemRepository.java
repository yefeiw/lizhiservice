package com.beikao.LizhiService.domain;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface BroadcastItemRepository extends MongoRepository<BroadcastItem,Integer> {
   //find by category
    List<BroadcastItem> findAllByCategory(@Param("username") String category);
    BroadcastItem findById(@Param("id") int id);
}
