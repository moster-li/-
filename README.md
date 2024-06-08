#题目来源于朋友分享，难度不高，用来作为一个简单程序设计任务了。
基于c语言开发的运动会管理系统
一、问题描述
参加运动会的一共有n个学校，学校编号分别为1, 2, …, n。项目积分为：5，3，1.使用c语言编写代码，完成以下功能。
二、设计要求
本课题要求同学们完成一个信息管理类的课题---《运动会成绩管理系统》，能够对运动会中的项目信息及比赛成绩进行有效地管理，实现项目成绩的录入、项目成绩信息查询、项目成绩信息统计等方面的基本操作。
管理内容（项目成绩信息）包括：
项目编号、项目名称、项目排名顺序、学校编号、学校名称、项目积分。
主要功能包括：
	录入项目成绩信息：
逐个录入每个项目的成绩信息，录入时，预先将所有项目的成绩信息存入文件中，再从文件中读取项目成绩信息。
	统计各个学校的总积分：
统计各个学校的所有项目的总积分，并将结果输出显示在屏幕上，打印格式：学校编号 项目总积分 
	按学校编号查询学校的总积分：
按学校编号从项目成绩信息中查找出与某个学校相关的项目成绩信息，并计算出所有相关项目的总积分并将结果显示在屏幕上，打印格式：学校编号 项目总积分 
	按学校编号查询学校的所有获奖项目：
按学校编号从项目成绩信息中查找出与某个学校相关的所有项目信息，并显示在屏幕上，打印格式：项目名称、项目排名顺序、项目积分
	按学校的总积分进行排序：
按着学校的所有项目的总积分对所有学校进行升序排序，并将排序结果显示在屏幕上，打印格式：学校编号 总积分
	按项目编号或名称查询项目信息：
按项目编号或项目名称查询与该项目相关的所有成绩信息，并将结果显示在屏幕上，打印格式：项目名称 项目排名顺序 学校编号 项目积分
	查询获奖项目最多的学校：
对每个学校的获奖项目进行统计，查找出获奖项目最多的学校，并将结果显示在屏幕上，打印格式：学校编号 获奖项目数
	数据保存：
将所有的项目成绩信息合理保存到磁盘上的文本文件中。
	退出系统：
程序运行结束，退出系统。
请选择（1-8，0：退出）
