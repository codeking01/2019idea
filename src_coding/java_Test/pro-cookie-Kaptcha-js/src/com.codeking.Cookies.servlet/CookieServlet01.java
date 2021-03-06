package com.codeking.Cookies.servlet;


import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * @author king_xiong
 * @date 2022-03-18 22:03
 */
@WebServlet("/cookie01")
public class CookieServlet01 extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //1.创建一个Cookie对象
        Cookie cookie = new Cookie("uname","tom");
        //2.将这个Cookie对象保存到浏览器端
        resp.addCookie(cookie);
        req.getRequestDispatcher("hello01.html").forward(req,resp);
    }
}
