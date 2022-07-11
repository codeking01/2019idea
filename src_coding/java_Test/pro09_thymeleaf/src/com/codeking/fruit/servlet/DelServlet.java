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
import java.util.List;

/**
 * @author king_xiong
 * @date 2022-01-23 11:45
 */
@WebServlet("/del.do")
public class DelServlet extends ViewBaseServlet {
    private FruitDAO fruitDAO = new FruitDAOimpl();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        //2.获取参数
        String fidStr = req.getParameter("fid");
        if (StringUtil.isNotEmpty(fidStr)){
            int fid = Integer.parseInt(fidStr);
            fruitDAO.delFruitList(fid);
            //重定向
            resp.sendRedirect("index");
        }
    }


}
