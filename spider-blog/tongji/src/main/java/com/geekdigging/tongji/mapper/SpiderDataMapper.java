package com.geekdigging.tongji.mapper;

import com.geekdigging.tongji.model.SpiderDataModel;
import org.apache.ibatis.annotations.Param;

import java.util.Date;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 *
 * @Date: 2019/11/2
 * @Time: 17:15
 * @email: inwsy@hotmail.com
 * Description:
 */
public interface SpiderDataMapper {
    // 查询增量数据
    List<SpiderDataModel> getIncrementalData(@Param("plantform") String plantform, @Param("start_date") Date start_date, @Param("end_date") Date end_date);

    // 查询累计数据
    List<SpiderDataModel> getAccumulatedData(@Param("plantform") String plantform, @Param("start_date") Date start_date, @Param("end_date") Date end_date);
}
