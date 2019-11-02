package com.geekdigging.tongji;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.geekdigging.tongji.mapper")
public class TongjiApplication {

    public static void main(String[] args) {
        SpringApplication.run(TongjiApplication.class, args);
    }

}
