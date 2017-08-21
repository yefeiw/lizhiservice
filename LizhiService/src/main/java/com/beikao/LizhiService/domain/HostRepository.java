package com.beikao.LizhiService.domain;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface HostRepository extends MongoRepository<Host,Integer>{
    Host findByHostName(String name);

}
