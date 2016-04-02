#function:
#compare two folders and all the subdirectory files
#print the common file name

#from filecmp import dircmp 
import os


fn1 = 'Pics_in_Apple'
fn2 = 'Pics_TOSHIBA'

#def print_same_files(dcmp):
#    for name in dcmp.same_files:
#        print ("common_file %s found in %s and %s.") % (name, dcmp.left, dcmp.right)
#    for sub_dcmp in dcmp.subdirs.values():
#        print_same_files(sub_dcmp)
#
#dcmp = dircmp(fn1, fn2) 
#print_same_files(dcmp) 



def print_all_files(fn):
    allfn = []
    for root, dirs, files in os.walk(fn):
#        print root, "consumes",
#        print sum(getsize(join(root, name)) for name in files),
#        print "bytes in", len(files), "non-directory files"
#        print root, files
        
        allfn = files + allfn
    return  allfn
    
af1 = print_all_files(fn1)
af2 = print_all_files(fn2)        


comfn = set(af1) & set(af2)

print ("These files : %s has same names") % comfn
