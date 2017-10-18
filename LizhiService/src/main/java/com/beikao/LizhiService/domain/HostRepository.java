package com.beikao.LizhiService.domain;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.query.Param;

public interface HostRepository extends MongoRepository<Host,String>{
    Host findByHostName(@Param("hostName") String hostName);

}
