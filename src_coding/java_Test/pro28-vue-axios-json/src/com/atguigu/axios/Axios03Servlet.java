package com.atguigu.axios;

import com.atguigu.pojo.User;
import com.google.gson.Gson;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;

@WebServlet("/axios03.do")
public class Axios03Servlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        //用来读每一行的内容
        StringBuffer stringBuffer = new StringBuffer("");
        //获取一个输入流
        BufferedReader bufferedReader = request.getReader();
        String str = null;
        while ((str = bufferedReader.readLine()) != null) {
            stringBuffer.append(str);
        }
        String requestBody = stringBuffer.toString();

        //已知 String
        //需要转化成 Java Object
        Gson gson = new Gson();

        //Gson有两个API
        //1.fromJson(string,T) 将字符串转化成java object
        //2.toJson(java Object) 将java object转化成json字符串，这样才能响应给客户端
        User user = gson.fromJson(requestBody, User.class);
        user.setUname("鸠摩智");
        user.setPwd("123456");
        System.out.println(requestBody);

        //假设user是从数据库查询出来的，现在需要将其转化成json格式的字符串，然后响应给客户端
        String userJsonStr = gson.toJson(user);
        response.setCharacterEncoding("UTF-8");
        //MIME-TYPE
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().write(userJsonStr);
    }
}
