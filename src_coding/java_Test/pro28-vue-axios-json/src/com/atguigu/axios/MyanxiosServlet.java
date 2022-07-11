package com.atguigu.axios;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * @author king_xiong
 * @date 2022-03-20 18:27
 */
@WebServlet("/myanxios01.do")
public class MyanxiosServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setCharacterEncoding("utf-8");

        String uname = req.getParameter("uname");
        String pwd = req.getParameter("pwd");

        System.out.println("uname = " + uname);
        System.out.println("pwd = " + pwd);

        resp.setCharacterEncoding("utf-8");
        resp.setContentType("text/html;charset=utf-8");

        //获取打印流
        PrintWriter out=resp.getWriter();
        out.write("uname"+"_"+pwd);

        //throw new NullPointerException("erro!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");

    }
}
