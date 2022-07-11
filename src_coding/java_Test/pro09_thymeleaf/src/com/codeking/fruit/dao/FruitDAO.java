package com.codeking.fruit.dao;

import com.codeking.fruit.pojo.Fruit;

import java.util.List;

/**
 * @author king_xiong
 * @date 2022-01-22 2:05
 */
public interface FruitDAO {
    //获取库存信息，fruitDAOimpl类会继承这个类 并且实现这个里面的方法
    //List<Fruit> getFruitList();

    //  根据主键fid查找库存
    Fruit getFruitListByFid(Integer fid);
    //修改指定的库存记录
    void updateFruitList(Fruit fruit);

    //根据指定的库存 删除记录
    void delFruitList(Integer fid);

    //添加
    void addFruit(Fruit fruit);

    //查询库存总数量
    int getFruitCount(String keyword);

    //获取指定页码上的库存信息  每页显示5条

    /**
     * 根据页码传递内容
     *
     * @param keyword
     * @param pageNo
     * @return
     */
    List<Fruit> getFruitList(String keyword, Integer pageNo);
}
