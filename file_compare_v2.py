#compare two folders and all the sub directories
#find the files under the same names and move them from folder 1 into a seperate folder

#from filecmp import dircmp 
import os
import os.path

fn1 = 'Pics_in_Apple'
#fn2 = 'Pics_TOSHIBA'
fn2 = 'duplicates'
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
comfn = list(comfn)
print ("These files : %s has same names") % comfn


def search_mov_fn(fnlist,foldern):
    newfoldername = "duplicates3"
    c_dir = os.getcwd()
    newpath = os.path.join(c_dir,newfoldername)
    os.makedirs(newpath)
    for root, dirs, files in os.walk(foldern):
        commonf = set(files) & set(fnlist)
        commonf = list(commonf)
        print root,commonf
        for i in range(len(commonf)):
            fp = os.path.join(root,commonf[i])
            np = os.path.join(newpath,commonf[i])
            os.rename(fp , np)           
            print ("%s has been moved to %s!!") % (fp, np)

search_mov_fn(comfn,fn1)
