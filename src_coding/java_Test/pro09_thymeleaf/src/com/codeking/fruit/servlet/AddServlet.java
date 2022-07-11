package com.codeking.fruit.servlet;

import com.codeking.fruit.dao.FruitDAO;
import com.codeking.fruit.dao.impl.FruitDAOimpl;
import com.codeking.fruit.pojo.Fruit;
import com.codeking.myssm.myspringMvc.ViewBaseServlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * @author king_xiong
 * @date 2022-01-23 14:53
 */
@WebServlet("/add.do")
public class AddServlet extends ViewBaseServlet {
    private FruitDAO fruitDAO = new FruitDAOimpl();

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //设置编码
        req.setCharacterEncoding("UTF-8");
        //获取参数
        String fname = req.getParameter("fname");
        Integer price = Integer.parseInt(req.getParameter("price"));
        Integer fcount = Integer.parseInt(req.getParameter("fcount"));
        String remark = req.getParameter("remark");

        Fruit fruit=new Fruit(0,fname,price,fcount,remark);
        fruitDAO.addFruit(fruit);

        //super.processTemplate("index",req,resp);
        resp.sendRedirect("index");

    }
}
