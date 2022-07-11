package com.codeking.myssm.utils;

/**
 * @author king_xiong
 * @date 2022-01-22 22:24
 */
public class StringUtil {
//    判断字符串非空
    public  static boolean isEmpty(String str) {
        return str==null || "".equals(str);
    }

    public static  boolean isNotEmpty(String str) {
        return !isEmpty(str);
    }
}
