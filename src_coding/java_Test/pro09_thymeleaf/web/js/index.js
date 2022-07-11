function delFruitList(fid) {
    if (confirm('是否确认删除？')) {
        //location 相当于浏览器地址栏对象  window 是这个窗口
        window.location.href = 'del.do?fid=' + fid;
    }
}

function page(pageNo){
    window.location.href="index?pageNo="+pageNo;
}
