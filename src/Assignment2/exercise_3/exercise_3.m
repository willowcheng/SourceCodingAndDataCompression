clc;
clear all;

%%%%Source Coding and Data Compression%%%%
%%%%Assignment 2, exercise 3
%%%%Author: Liu Cheng

dimen='512 512';
maxVal = '255';
 
% red and green color by 512 x 512 
file=fopen('cube_red_green.ppm','w');
fprintf(file,'P3\n%s\n%s\n', dimen, maxVal);
for i=1:512
    for j=1:512
        x_color = fix((i - 1) / 2);
        y_color = fix((j - 1) / 2);
        fprintf(file, '%d %d 0 ', x_color, y_color);
    end
    fprintf(file, '\n');
end
fclose(file);


% blue and green color by 512 x 512 
file=fopen('cube_blue_green.ppm','w');
fprintf(file,'P3\n%s\n%s\n', dimen, maxVal);
for i=1:512
    for j=1:512
        x_color = fix((i - 1) / 2);
        y_color = fix((j - 1) / 2);
        fprintf(file, '0 %d %d ', y_color, x_color);
    end
    fprintf(file, '\n');
end
fclose(file);

% blue and red color by 512 x 512 
file=fopen('cube_blue_red.ppm','w');
fprintf(file,'P3\n%s\n%s\n', dimen, maxVal);
for i=1:512
    for j=1:512
        x_color = fix((i - 1) / 2);
        y_color = fix((j - 1) / 2);
        fprintf(file, '%d 0 %d ', y_color, x_color);
    end
    fprintf(file, '\n');
end
fclose(file);

% cyan and yellow color by 512 x 512 
file=fopen('cube_cyan_yellow.ppm','w');
fprintf(file,'P3\n%s\n%s\n', dimen, maxVal);
for i=1:512
    for j=1:512
        x_color = fix((i - 1) / 2);
        y_color = fix((j - 1) / 2);
        fprintf(file, '%d 255 %d ', y_color, x_color);
    end
    fprintf(file, '\n');
end
fclose(file);

% magenta and cyan color by 512 x 512 
file=fopen('cube_magenta_cyan.ppm','w');
fprintf(file,'P3\n%s\n%s\n', dimen, maxVal);
for i=1:512
    for j=1:512
        x_color = fix((i - 1) / 2);
        y_color = fix((j - 1) / 2);
        fprintf(file, '%d %d 255 ', x_color, y_color);
    end
    fprintf(file, '\n');
end
fclose(file);


% magenta and yellow color by 512 x 512 
file=fopen('cube_magenta_yellow.ppm','w');
fprintf(file,'P3\n%s\n%s\n', dimen, maxVal);
for i=1:512
    for j=1:512
        x_color = fix((i - 1) / 2);
        y_color = fix((j - 1) / 2);
        fprintf(file, '255 %d %d ', y_color, x_color);
    end
    fprintf(file, '\n');
end
fclose(file);