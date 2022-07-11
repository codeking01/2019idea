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
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.List;

/**
 * @author king_xiong
 * @date 2022-01-22 2:23
 */
//Servlet从3.0版本开始支持注解方式的注册
@WebServlet("/index")
public class IndexServlet extends ViewBaseServlet {
    //由于这个查询功能 大部分还是复用doGet里面的内容
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //由于复用了代码 所以这个设置一下编码
        req.setCharacterEncoding("UTF-8");

        //用session来记录这个传入的参数
        HttpSession session = req.getSession();
        String oper = req.getParameter("oper");
        //因为这个点击查询这个位置加了个隐藏域 oper  如果是从查询点击过来的 可以识别出
        //如果是null的话 就是从其他按钮点击的

        //获取当前页码 默认为1  这个是第一次做渲染的
        Integer pageNo = 1;
        String keyword = null;
        if (StringUtil.isNotEmpty(oper) && "search".equals(oper)) {
            //说明是点击表单查询发送过来的请求
            //此时，pageNo应该还原为1 ， keyword应该从请求参数中获取
            pageNo = 1;
            keyword = req.getParameter("keyword");
            if (StringUtil.isEmpty(keyword)) {
                //当什么也没输入的时候 keyword为null  这个地方我们把它设置为空
                keyword = "";
            }
            //传入session
            session.setAttribute("keyword", keyword);
        } else {
            //这个是通过点击 页面上的其他选项 比如下一页等操作的时候 会改变这个pageNo 然后再去通过session重新赋值
            String pageNoStr = req.getParameter("pageNo");
            if (StringUtil.isNotEmpty(pageNoStr)) {
                pageNo = Integer.parseInt(pageNoStr);
            }
            Object keywordObj = session.getAttribute("keyword");
            if (keywordObj != null) {
                keyword = (String) keywordObj;
            } else {
                //这个是处理第一次查询的情况（第一次加载页面的情况）
                keyword = "";
            }

        }
        //把当前页码传递给session 更新当前页的值
        session.setAttribute("pageNo", pageNo);

        FruitDAO fruitDAO = new FruitDAOimpl();
        //根据当前页码传递  内容 查询内容（一次5个 我这个在方法里写死了）
        List<Fruit> fruitList = fruitDAO.getFruitList(keyword, pageNo);
        //保存到session作用域
        session.setAttribute("fruitList", fruitList);
        //总记录条数
        int fruitCount = fruitDAO.getFruitCount(keyword);
        //总页数
        int pageCount = (fruitCount + 5 - 1) / 5;
            /*
            总记录条数       总页数
            1               1
            5               1
            6               2
            10              2
            11              3
            fruitCount      (fruitCount+5-1)/5
             */
        session.setAttribute("pageCount", pageCount);

        //此处的视图名称是 index
        //那么thymeleaf会将这个 逻辑视图名称 对应到 物理视图 名称上去
        //逻辑视图名称 ：   index
        //物理视图名称 ：   view-prefix + 逻辑视图名称 + view-suffix
        //所以真实的视图名称是：      /       index       .html
        System.out.println("开始渲染页面！！");
        super.processTemplate("index", req, resp);
    }
}
