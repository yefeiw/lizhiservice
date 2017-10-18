package com.beikao.LizhiService.domain;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface BroadcastItemRepository extends MongoRepository<BroadcastItem,String> {
   //find by category
    List<BroadcastItem> findAllByCategory(@Param("category") String category);
    BroadcastItem findById(@Param("id") String id);
}
