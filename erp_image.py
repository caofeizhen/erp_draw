import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = ['load_congruency_fear.csv', 'load_congruency_happy.csv', 'load_uncongruency_fear.csv',
       'load_uncongruency_happy.csv',
       'no_congruency_fear.csv', 'no_congruency_happy.csv', 'no_uncongruency_fear.csv', 'no_uncongruency_happy.csv']

def print_brainvs_n(channel,conditiona,conditionb,fillstart,fillend,name):
       channel=channel
       path='/Users/caofeizhen/Desktop/channel/'+channel+'/'+con[conditiona]
       file=pd.read_csv(path,header=None)
       file=file.mean(axis=0)
       filey=np.array(file)
       filex=np.arange(-200,800)

       path2='/Users/caofeizhen/Desktop/channel/'+channel+'/'+con[conditionb]
       file2=pd.read_csv(path2,header=None)
       file2=file2.mean(axis=0)
       filey2=np.array(file2)



       plt.figure() #设置图片和坐标轴

       plt.plot(filex,filey,linewidth=1.5,label=con[conditiona][:-4])
       plt.plot(filex,filey2,linewidth=1.5,label=con[conditionb][:-4])
       plt.legend(loc='best')#打印图例

       plt.xlim((-200,800))
       plt.ylim((-10,15))
       plt.xlabel(r'$Time(ms)$')
       plt.ylabel((r'$Potential(uV)$'))

       new_ticks=np.arange(-200,800,100)
       plt.xticks(new_ticks)
       plt.yticks(np.array([-10,-5,5,10,15]))

       y0=np.min(filey[fillstart+200:fillend+200])#标记脑电成分
       x0=np.where(filey==np.min(filey[fillstart+200:fillend+200]))[0][0]-200
       plt.annotate(name,xy=(x0,y0),xycoords='data',xytext=(+10,-10),textcoords='offset points',color='red',size=10)



       plt.fill_between(filex,-15,where=(filex>fillstart)&(filex<fillend),facecolor='grey',alpha=.25)
       plt.fill_between(filex,15,where=(filex>fillstart)&(filex<fillend),facecolor='grey',alpha=.25)



       ax=plt.gca()  #移动坐标轴
       ax.spines['top'].set_color('none')
       ax.spines['right'].set_color('none')
       ax.xaxis.set_ticks_position('bottom')
       ax.yaxis.set_ticks_position('left')
       ax.spines['bottom'].set_position(('data',0))
       ax.spines['left'].set_position(('data',0))


       plt.show()


def print_brainvs_p(channel, conditiona, conditionb, fillstart, fillend, name):
       channel = channel
       path = '/Users/caofeizhen/Desktop/channel/' + channel + '/' + con[conditiona]
       file = pd.read_csv(path, header=None)
       file = file.mean(axis=0)
       filey = np.array(file)
       filex = np.arange(-200, 800)

       path2 = '/Users/caofeizhen/Desktop/channel/' + channel + '/' + con[conditionb]
       file2 = pd.read_csv(path2, header=None)
       file2 = file2.mean(axis=0)
       filey2 = np.array(file2)

       plt.figure()  # 设置图片和坐标轴

       plt.plot(filex, filey, linewidth=1.5, label=con[conditiona][-4])
       plt.plot(filex, filey2, linewidth=1.5, label=con[conditionb][-4])
       plt.legend(loc='best')  # 打印图例

       plt.xlim((-200, 800))
       plt.ylim((-10, 15))
       plt.xlabel(r'$Time(ms)$')
       plt.ylabel((r'$Potential(uV)$'))

       new_ticks = np.arange(-200, 800, 100)
       plt.xticks(new_ticks)
       plt.yticks(np.array([-10, -5, 5, 10, 15]))

       y0 = np.min(filey[fillstart + 200:fillend + 200])  # 标记脑电成分
       x0 = np.where(filey == np.max(filey[fillstart + 200:fillend + 200]))[0][0] - 200
       plt.annotate(name, xy=(x0, y0), xycoords='data', xytext=(+10, -10), textcoords='offset points', color='red',
                    size=10)

       plt.fill_between(filex, -15, where=(filex > fillstart) & (filex < fillend), facecolor='grey', alpha=.25)
       plt.fill_between(filex, 15, where=(filex > fillstart) & (filex < fillend), facecolor='grey', alpha=.25)

       ax = plt.gca()  # 移动坐标轴
       ax.spines['top'].set_color('none')
       ax.spines['right'].set_color('none')
       ax.xaxis.set_ticks_position('bottom')
       ax.yaxis.set_ticks_position('left')
       ax.spines['bottom'].set_position(('data', 0))
       ax.spines['left'].set_position(('data', 0))

       plt.show()



con = ['load_congruency_fear.csv', 'load_congruency_happy.csv', 'load_uncongruency_fear.csv',
       'load_uncongruency_happy.csv',
       'no_congruency_fear.csv', 'no_congruency_happy.csv', 'no_uncongruency_fear.csv', 'no_uncongruency_happy.csv']
print_brainvs_n(channel='FCZ',conditiona=1,conditionb=3,fillstart=360,fillend=450,name='N400')