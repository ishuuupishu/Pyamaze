from pyamaze import maze,agent
# m  = maze(5,5)
# m.CreateMaze()
# m.run(); 
m = maze(20,35)
m.CreateMaze(x=1,y=1,theme='dark')

a = agent(m,filled=True,footprints=True)
m.tracePath({a:m.path})

print(m.maze_map)
m.run()