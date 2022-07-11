package com.codeking.fruit.servlet;

import com.codeking.fruit.dao.FruitDAO;
import com.codeking.fruit.dao.impl.FruitDAOimpl;
import com.codeking.fruit.pojo.Fruit;
import com.codeking.myssm.myspringMvc.ViewBaseServlet;
import com.codeking.myssm.utils.StringUtil;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * @author king_xiong
 * @date 2022-01-22 23:37
 */
@WebServlet("/update.do")
public class UpdateServlet extends ViewBaseServlet {
    private FruitDAO fruitDAO = new FruitDAOimpl();

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //1.设置编码
        req.setCharacterEncoding("utf-8");

        //2.获取参数
        String fidStr = req.getParameter("fid");
        Integer fid = Integer.parseInt(fidStr);
        String fname = req.getParameter("fname");
        String priceStr = req.getParameter("price");
        int price = Integer.parseInt(priceStr);
        String fcountStr = req.getParameter("fcount");
        Integer fcount = Integer.parseInt(fcountStr);
        String remark = req.getParameter("remark");

        //3.执行更新
        fruitDAO.updateFruitList(new Fruit(fid, fname, price, fcount, remark));

        //设置重定向  这个位置不要写 内部转发
        resp.sendRedirect("index");

    }
}
