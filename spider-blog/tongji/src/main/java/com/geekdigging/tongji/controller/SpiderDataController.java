package com.geekdigging.tongji.controller;

import com.geekdigging.tongji.mapper.SpiderDataMapper;
import com.geekdigging.tongji.model.SpiderDataModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 *
 * @Date: 2019/11/2
 * @Time: 17:23
 * @email: inwsy@hotmail.com
 * Description:
 */
@Controller
@RequestMapping("/spider")
public class SpiderDataController {
    @Autowired
    SpiderDataMapper spiderDataMapper;

    @GetMapping("/index")
    public String index() {
        return "index";
    }

    @GetMapping("/getIncrementalData")
    @ResponseBody
    public List<SpiderDataModel> getIncrementalData(@RequestParam("plantform") String plantform, @RequestParam("start_date") @DateTimeFormat(pattern="yyyy-MM-dd") Date start_date, @RequestParam("end_date") @DateTimeFormat(pattern="yyyy-MM-dd") Date end_date) {
        return spiderDataMapper.getIncrementalData(plantform, start_date, end_date);
    }

    @GetMapping("/getAccumulatedData")
    @ResponseBody
    public List<SpiderDataModel> getAccumulatedData(@RequestParam("plantform") String plantform, @RequestParam("start_date") @DateTimeFormat(pattern="yyyy-MM-dd") Date start_date, @RequestParam("end_date") @DateTimeFormat(pattern="yyyy-MM-dd") Date end_date) {
        return spiderDataMapper.getAccumulatedData(plantform, start_date, end_date);
    }
}
