/*
 * Function:
 * pick out the files with duplicate names;
 * print out the names;
 * used for finding out the duplicate photos from two folders
 * 04/01/2016
 */
import java.io.*;

public class duplicateFile {
	public static void main(String[] args) {
		File f1 = new File("/Users/graceqin/Documents"); // first folder's absolute path
		File f2 = new File("/Users/graceqin/Documents"); // second folder's absolute path
		String[] l1 = f1.list();
		String[] l2 = f2.list(); 
		String fn1;
		String fn2;
		String dupes = "";

		for (int i = 0; i < l1.length; i++) {
			fn1 = l1[i];
			for (int j =0; j < l2.length; j++) {
				fn2 = l2[j];
				if(fn1.equals(fn2)) {
					dupes = dupes + fn1 + " / ";
				}
			}
		}

		// print out the duplicate file names
		System.out.println("*******************************");
		System.out.println("The duplicate files are: " + dupes);
	}
}