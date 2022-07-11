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
 * @date 2022-01-22 15:55
 */
@WebServlet("/edit.do")
//点击编辑页面会跳转到这个servlet类，然后通过查询数据库从而再渲染页面
public class EditServlet extends ViewBaseServlet {
    //用这个 fruitDAO 来操作数据库(在这里 这个是查询)
    private FruitDAO fruitDAO = new FruitDAOimpl();

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String fidStr = req.getParameter("fid");
        if (StringUtil.isNotEmpty(fidStr)) {
            int fid = Integer.parseInt(fidStr);
            //通过fid去查询库存
            Fruit fruit = fruitDAO.getFruitListByFid(fid);
            req.setAttribute("fruit", fruit);
            //渲染页面
            super.processTemplate("edit", req, resp);
        }
        else{
            System.out.println("空的！！");
        }
    }
}
