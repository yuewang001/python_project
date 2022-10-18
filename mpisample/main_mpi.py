#D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Lib\site-packages\mpi4py
import sys
sys.path.append(r'D:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_64\\Lib\\site-packages\\mpi4py')
print(sys.path)
#import mpi4py.MPI as MPI
from mpi4py import MPI
import  mpi4py as MPI
print("begin to run ....")
#print( "my rank is %d" % MPI.COMM_WORLD.Get_rank() )
#print(mpi4py.__all__)
MPI.profile
comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()