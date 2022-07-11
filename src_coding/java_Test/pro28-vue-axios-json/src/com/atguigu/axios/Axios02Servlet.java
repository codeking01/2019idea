package com.atguigu.axios;

import com.atguigu.pojo.User;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/axios02.do")
public class Axios02Servlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 2.创建StringBuilder对象来累加存储从请求体中读取到的每一行
        StringBuffer stringBuffer = new StringBuffer("");

        //用一个bufferedReader去读数据
        // 1.由于请求体数据有可能很大，所以Servlet标准在设计API的时候要求我们通过输入流来读取
        BufferedReader bufferedReader = request.getReader();

        // 3.声明临时变量
        String str = null ;
        // 4.循环读取
        while((str=bufferedReader.readLine())!=null){
            stringBuffer.append(str);
        }

        // 5.关闭流  这个可以不关闭  因为这个流不是new出来的
        //bufferedReader.close();

        // 6.累加的结果就是整个请求体
        str = stringBuffer.toString() ;
        System.out.println(str);

        //已知 String
        //需要转化成 Java Object

        // 7.创建Gson对象用于解析JSON字符串
        Gson gson = new Gson();
        //Gson有两个API
        //1.fromJson(string,T) 将字符串转化成java object
        //2.toJson(java Object) 将java object转化成json字符串，这样才能响应给客户端

        User user = gson.fromJson(str, User.class);
        user.setUname("李白");
        user.setPwd("123456");
        System.out.println(str);

        //把user对象转化为json格式
        String userJsonStr =gson.toJson(user);
        response.setCharacterEncoding("UTF-8");

        //MIME-TYPE MIME格式
        response.setContentType("application/json;charset=utf-8");
        response.getWriter().write(userJsonStr);

        System.out.println(user);
    }
}
