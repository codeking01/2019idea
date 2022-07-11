package com.codeking.boot.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author king_xiong
 * @date 2022-02-04 12:37
 */

@RestController
public class HelloController {
    //用RequestMapping 取代了xml中配置servlet
    @RequestMapping("/hello")
    public String handle01() {
        return "Hello,spring boot 2"+"，你好呵呵哈哈哈  ";
    }
}
