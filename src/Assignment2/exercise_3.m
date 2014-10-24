clear all;

%%%%Source Coding and Data Compression%%%%
%%%%Assignment 2, exercise 3
%%%%Author: Liu Cheng
red='1 0 0 ';
green='0 1 0 ';
blue='0 0 1 ';
cyan='0 1 1 ';
yellow='1 1 0 ';
magenta='1 0 1 ';
dimen='512 512 1';
 
% red color by 512 x 512 
file=fopen('red.ppm','w');
fprintf(file,'P3\n%s\n',dimen);
for i=1:512
    for j=1:512
        fprintf(file,red);
    end
    fprintf(file, '\n');
end
fclose(file);


% blue color by 512 x 512 
file=fopen('blue.ppm','w');
fprintf(file,'P3\n%s\n',dimen);
for i=1:512
    for j=1:512
        fprintf(file,blue);
    end
    fprintf(file, '\n');
end
fclose(file);

% green color by 512 x 512 
file=fopen('green.ppm','w');
fprintf(file,'P3\n%s\n',dimen);
for i=1:512
    for j=1:512
        fprintf(file,green);
    end
    fprintf(file, '\n');
end
fclose(file);

% cyan color by 512 x 512 
file=fopen('cyan.ppm','w');
fprintf(file,'P3\n%s\n',dimen);
for i=1:512
    for j=1:512
        fprintf(file,cyan);
    end
    fprintf(file, '\n');
end
fclose(file);

% yellow color by 512 x 512 
file=fopen('yellow.ppm','w');
fprintf(file,'P3\n%s\n',dimen);
for i=1:512
    for j=1:512
        fprintf(file,yellow);
    end
    fprintf(file, '\n');
end
fclose(file);


% magenta color by 512 x 512 
file=fopen('magenta.ppm','w');
fprintf(file,'P3\n%s\n',dimen);
for i=1:512
    for j=1:512
        fprintf(file,magenta);
    end
    fprintf(file, '\n');
end
fclose(file);