import matplotlib.pyplot as plt
import matplotlib
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

def plotMap(carData,roadData,crossData):
    print('plotMap')
    rel={'up':-1,
         'right':-1,
         'down':-1,
         'left':-1,
         'length_up':-1,
         'length_right':-1,
         'length_down':-1,
         'length_left':-1,
         'roadUp': -1,
         'roadRight': -1,
         'roadDown': -1,
         'roadLeft': -1,
         }
    map=[]
    n=len(crossData['id'])#道路节点个数
    for i in range(n):
        rel=rel.copy()
        rel['up']=crossData['roadUp'][i]
        rel['right'] = crossData['roadRight'][i]
        rel['down'] = crossData['roadDown'][i]
        rel['left'] = crossData['roadLeft'][i]
        rel['roadUp'] = crossData['roadUp'][i]
        rel['roadRight'] = crossData['roadRight'][i]
        rel['roadDown'] = crossData['roadDown'][i]
        rel['roadLeft'] = crossData['roadLeft'][i]
        map.append(rel)

    for idx,val in enumerate(map):
        id=str(idx+1)
        up=val['up']
        right=val['right']
        down=val['down']
        left=val['left']
        flag=0
        for idx_,val_ in enumerate(roadData['id']):
            if flag==4:
                break
            if up==val_:
                map[idx]['up']=next_point(id,roadData['from'][idx_],roadData['to'][idx_])
                map[idx]['length_up'] = roadData['length'][idx_]
                flag=flag+1
            elif right==val_:
                map[idx]['right']=next_point(id,roadData['from'][idx_],roadData['to'][idx_])
                map[idx]['length_right'] = roadData['length'][idx_]
                flag=flag+1
            elif down == val_:
                map[idx]['down'] = next_point(id, roadData['from'][idx_], roadData['to'][idx_])
                map[idx]['length_down'] = roadData['length'][idx_]
                flag = flag + 1
            elif left == val_:
                map[idx]['left'] = next_point(id, roadData['from'][idx_], roadData['to'][idx_])
                map[idx]['length_left'] = roadData['length'][idx_]
                flag = flag + 1

    idx_list=[]
    #初始点位置(0,0)
    point_x=[-1]*n
    point_y=[-1]*n
    point_x[0]=0
    point_y[0]=0
    idx_list.append(0)
    for idx,val in enumerate(map):
        up = int(val['up'])-1
        right = int(val['right'])-1
        down = int(val['down'])-1
        left = int(val['left'])-1
        length_up = int(val['length_up'])
        length_right = int(val['length_right'])
        length_down = int(val['length_down'])
        length_left = int(val['length_left'])
        if up!=-2:
            if up not in idx_list:
                point_x[up]=point_x[idx]
                point_y[up] = point_y[idx]+length_up
                idx_list.append(up)
        if right!=-2:
            if right not in idx_list:
                point_x[right]=point_x[idx]+length_right
                point_y[right] = point_y[idx]
                idx_list.append(right)
        if down!=-2:
            if down not in idx_list:
                point_x[down]=point_x[idx]
                point_y[down] = point_y[idx]-length_down
                idx_list.append(down)
        if left!=-2:
            if left not in idx_list:
                point_x[left]=point_x[idx]-length_left
                point_y[left] = point_y[idx]
                idx_list.append(left)


    # 画图
    plt.figure(num=1, figsize=(10, 6))  # 定义一个图像窗口，编号为1，大小(10,6)
    # 画点
    plt.plot(point_x, point_y, 'o', color='green', markersize=10)  # 画点，设置点的样式，颜色，大小
    plt.title('地图', fontsize=50)
    for i in range(n):
        plt.text(point_x[i],point_y[i],str(i+1))

    # 画线
    for idx,val in enumerate(map):
        up = int(val['up'])-1
        right = int(val['right'])-1
        down = int(val['down'])-1
        left = int(val['left'])-1
        if up!=-2:
            plt.plot([point_x[idx],point_x[up]],[point_y[idx],point_y[up]])
            plt.text((point_x[idx]+point_x[up])/2,(point_y[idx]+point_y[up])/2, str(map[idx]['roadUp']))
        if right!=-2:
            plt.plot([point_x[idx], point_x[right]], [point_y[idx], point_y[right]])
            plt.text((point_x[idx]+ point_x[right])/2, (point_y[idx]+ point_y[right])/2, str(map[idx]['roadRight']))
        if down!=-2:
            plt.plot([point_x[idx], point_x[down]], [point_y[idx], point_y[down]])
            # plt.text((point_x[idx]+point_x[down])/2,(point_y[idx]+ point_y[down])/2, 'down')
        if left!=-2:
            plt.plot([point_x[idx], point_x[left]], [point_y[idx], point_y[left]])
            # plt.text((point_x[idx]+point_x[left])/2, (point_y[idx]+ point_y[left])/2, 'left')

    plt.show()
    print('over')

def next_point(val,from_,to_):
    return to_ if val==from_ else from_