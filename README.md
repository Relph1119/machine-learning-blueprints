#记录自己学习《Python 机器学习实践指南》这本书的全部过程#

本书上传的所有代码都是可以运行的，在此附上本书的github地址：
[https://github.com/PacktPublishing/Python-Machine-Learning-Blueprints](https://github.com/PacktPublishing/Python-Machine-Learning-Blueprints)

## 运行环境 ##
Python 版本：3.6.2<br/>
PyCharm 版本：PyCharm 2017.3.3 (Professional Edition)

## 代码结构 ##
<pre>
src
+---ch1
|    +----groupby_learning.py--------------聚类函数示例
|    +----matpolotlib_bar.py---------------推积条形图展示
|    +----matpolotlib_hist.py--------------直方图展示
|    +----matpolotlib_plot.py--------------折线图展示
|    +----matpolotlib_scatter.py-----------散点图展示
|    +----matpolotlib_subplots.py----------多图展示
|    +----pandas_learning.py---------------获取Iris数据
|    +----scikit_test1.py------------------scikit评估预测示例
|    +----scikit_test2.py
|    +----seabarn_learning.py
|    +----seabarn_violin.py----------------seabarn小提琴图展示
|    +----statsmodels_learning.py----------建模：回归模型示例
+---ch2
|    +----analysisData.py------------------分析数据
|    +----getMagicData.py------------------得到公寓的数据并进行数据清理
|    +----modelingData.py------------------对数据建模
|    +----predictData.py-------------------预测（不知道什么原因，代码报错，目前还没有找到解决办法，追踪了源码，仍未解决）
|    +----showData.py----------------------可视化数据（由于没有地理json，该代码无法运行）
+---ch3
|    +----getTicketsData.py----------------获得机票数据（由于跳转到中文版页面，获取数据的代码还需要重写，没有完成）
|    +----seleniumTest.py------------------爬虫测试代码，获取当天斗鱼的房间名和人气数
+---ch4
|    +----analysisData.py------------------分析IPO数据
|    +----analysisFeature.py---------------分析特征重要性，拟合随机森林分类器
|    +----getFeature.py--------------------特征工程，获取特征值
|    +----getIPOData.py--------------------获取IPO数据
|    +----predictData_2014_0.25.py---------分析2014年之后的数据，阈值=1
|    +----predictData_2015_0.25.py---------分析2015年之后的数据，阈值=0.25
|    +----predictData_2015_1.py------------二元分类，分析2015年之后的数据，阈值=1
+---ch7
|    +----analysisData.py------------------分析数据
|    +----analysisData_extend.py-----------分析延伸数据
|    +----ch7utils.py----------------------展示在策略的统计信息
|    +----dynamicTimeWarping.py------------动态时间扭曲算法（该算法需要运行821*821次，需要计算大约65万次，如果用单机跑，会很慢）
|    +----getData.py-----------------------获取SPY2010-2016年数据
|    +----getData_extend.py----------------获取SPY2000-2016年数据
|    +----getModel_extend_1000.py----------选择最后1000个作为测试节点
|    +----getModel_extend_2000.py----------选择最后2000个作为测试节点
+---ch8
|    +----chi2kernel.py--------------------卡方核算法
|    +----cosineSimilarity.py--------------余弦相似性算法
|    +----getDigitsData.py-----------------加载MNIST手写数字数据库
+---ch9
|    +----eliza_chat.py--------------------NLTK的聊天机器人Demo程序
|    +----getData.py-----------------------加载nscb.csv数据
|    +----getSimilarityAnswers.py----------简易版的聊天机器人
+---ch10
|    +----cntrdCoSim.py--------------------基于项目的过滤示例
|    +----getSimilarity.py-----------------进行相似性预测和评估
|    +----getStarted.py--------------------得到本人自己的github打star的数据
\---data
     +----ipo_data.csv---------------------第四章IPO数据
     +----iris.data------------------------第一章数据
     +----magic.csv------------------------第二章公寓数据
     +----nscb.csv-------------------------第九章聊天数据集
     +----SCOOP-Rating-Performance.xls-----SCOOP的所有指数数据，可参考书中下载
     +----spy.csv
     +----spy_2000_2016.csv----------------SPY2000年-2016年数据
     +----spy_2010_2016.csv----------------SPY2010年-2016年数据
doc
+---基于序列到序列模型的神经网络构造.pdf-------此为本书推荐需要看的论文
</pre>

## 运行结果 ##
第九章-简易聊天机器人的运行截图
![](https://i.imgur.com/W656E0U.png)

## 总结 ##
&emsp;&emsp;看完整本书用了10天左右，在单机上运行了实验代码，并在其中做了很多兼容性调整，书中有一部分代码在Jupyter Notebook下运行会提示警告，上传的代码中已经消除。<br/>
&emsp;&emsp;本书为了通过介绍机器学习来对各个领域进行初步的了解，比如NLP（自然语言处理）、图像识别、深度学习、推荐引擎、基本爬虫知识以及量化交易。

<font color=red>**说明**：</font><br/>
**1.** 第二章中的预测代码错误还未解决，以后会花时间解决。<br/>
**2.** 由于第五章和第六章的数据获取不到，不能编写实验代码。<br/>
**3.** 第八章由于graphlab目前只能支持Python2.7，不能支持Python3.X，故不能进行深度学习实验。<br/>
**4.** 第九章的聊天机器人的实验非常棒，建议亲手试试看。<br/>
**5.** 上述项目没有设计任何部署的步骤。