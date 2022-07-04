import java.io.File;
import java.util.Arrays;
import java.util.Random;

public class Tree {
    private String[] extensions = {".exe", ".jar", ".zip", ".rar", ".mp3", ".mp4", ".avi", ".png", ".jpg", ".bin", ".7z", ".ps4",
    ".sys", ".dll", ".txt", ".tif", ".tiff", ".bat", ".doc", ".gif", ".ini", ".html", ".mpeg", ".msi", ".pdf"};
    private int leftLimit = 97; // letter 'a'
    private int rightLimit = 122; // letter 'z'

    public static void main(String[] args) {
        String directory = ".";
        if (args.length > 0) {
            directory = args[0];
        }
        Random random = new Random(123456789);
        (new Tree()).Traversal(new File(directory), "", random);
    }
    public Tree() {}
    private String GenerateString(Random random)
    {
        int length = random.nextInt(50 - 0 + 1) + 0;
        StringBuilder buffer = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            int randomLimitedInt = leftLimit + (int)
                    (random.nextFloat() * (rightLimit - leftLimit + 1));
            buffer.append((char) randomLimitedInt);
        }
        return buffer.toString() + extensions[random.nextInt(extensions.length)];
    }
    private void Traversal(File folder, String prefix, Random random) {
        File file, fileList[] = folder.listFiles();
        if(fileList != null)
        {
            Arrays.sort(fileList);
            for (int i = 0; i < fileList.length; i++)
            {
                long r1 = random.nextLong(fileList.length - 0 + 1) + 0;
                file = fileList[i];
                if (file.getName().charAt(0) == '.') {
                    continue;
                }
                if (i == fileList.length - 1) {
                    if(r1 == i && i > 0)
                    {
                        System.out.println(prefix + "└── " + GenerateString(random));
                        i /= r1;
                        if (file.isDirectory()) Traversal(file, prefix + "    ", random);
                    }
                    else
                    {
                        System.out.println(prefix + "└── " + file.getName());
                        if (file.isDirectory()) Traversal(file, prefix + "    ", random);
                    }
                } else {
                    if(r1 == i && i > 0)
                    {
                        System.out.println(prefix + "├── " + GenerateString(random));
                        i /= r1;
                        if (file.isDirectory()) Traversal(file, prefix + "│   ", random);
                    }
                    else {
                        System.out.println(prefix + "├── " + file.getName());
                        if (file.isDirectory()) Traversal(file, prefix + "│   ", random);
                    }
                }
            }
        }
    }
}