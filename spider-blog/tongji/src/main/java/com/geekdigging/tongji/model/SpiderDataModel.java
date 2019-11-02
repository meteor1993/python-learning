package com.geekdigging.tongji.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Date;

/**
 * Created with IntelliJ IDEA.
 *
 * @Date: 2019/11/2
 * @Time: 17:12
 * @email: inwsy@hotmail.com
 * Description:
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class SpiderDataModel {
    private String id;
    private String plantform;
    private int read_num;
    private int fans_num;
    private int rank_num;
    private int like_num;
    private Date create_date;
}
