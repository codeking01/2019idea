package com.codeking.fruit.dao.impl;

import com.codeking.fruit.dao.FruitDAO;
import com.codeking.fruit.pojo.Fruit;
import com.codeking.myssm.basedao.BaseDAO;

import java.util.List;

/**
 * @author king_xiong
 * @date 2022-01-22 2:09
 */
public class FruitDAOimpl extends BaseDAO<Fruit> implements FruitDAO {
    //@Override
    //public List<Fruit> getFruitList() {
    //    return super.executeQuery("select * from t_fruit");
    //}

    @Override
    public Fruit getFruitListByFid(Integer fid) {
        return super.load("select * from t_fruit where fid=?", fid);
    }

    @Override
    public void updateFruitList(Fruit fruit) {
        String sql = "update t_fruit set fname=?,price=?,fcount=?,remark=? where fid=?";
        super.executeUpdate(sql, fruit.getFname(), fruit.getPrice(), fruit.getFcount(), fruit.getRemark(), fruit.getFid());
    }

    //删除
    @Override
    public void delFruitList(Integer fid) {
        super.executeUpdate("delete from t_fruit where fid=?", fid);
    }

    //添加
    @Override
    public void addFruit(Fruit fruit) {
        String sql = "insert into t_fruit values(0,?,?,?,?)";
        //会返回一个自增的 主键fid的值 现在我们接触不到  书城项目会看到
        super.executeUpdate(sql, fruit.getFname(), fruit.getPrice(), fruit.getFcount(), fruit.getRemark());
    }

    @Override
    public int getFruitCount(String keyword) {
        return ((Long) super.executeComplexQuery("select count(*) from t_fruit  where fname like ? or remark like ?","%"+keyword+"%","%"+keyword+"%")[0]).intValue();
    }

    @Override
    public List<Fruit> getFruitList(String keyword, Integer pageNo) {
        //这个5代表一页显示五个 一次从数据库里面取出5个
        return super.executeQuery("select * from t_fruit where fname like ? or remark like ? limit ?,5","%"+keyword+"%","%"+keyword+"%",(pageNo-1)*5);
    }
}
