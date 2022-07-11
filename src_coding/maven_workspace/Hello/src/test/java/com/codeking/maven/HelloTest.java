package com.codeking.maven;

import com.codeking.Hello;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * @author king_xiong
 * @date 2022-02-04 11:17
 */
public class HelloTest {

    @Test
    public void sayHello() {
        Hello hello = new Hello();
        String maven = hello.sayHello("Maven");
        System.out.println(maven);
    }
}