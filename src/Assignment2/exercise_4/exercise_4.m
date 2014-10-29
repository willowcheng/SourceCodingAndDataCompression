clear all;

%%%%Source Coding and Data Compression%%%%
%%%%Assignment 2, exercise 4
%%%%Author: Liu Cheng

% be ware that this script is depended on huffman_table_CCITT_group3.m
% please include all images, white_runlength.txt and
% black_runlength.txt

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% huffman code table

% generate huffman table for white and black values
fid = fopen('white_runlength.txt', 'r');

% calculate rows of runlength table
line_count = 0;
tline = fgetl(fid);
while ischar(tline)
    tline = fgetl(fid);
    line_count = line_count+1;
end
fclose(fid);

% store values of indicies and run_length huffman code
fid = fopen('white_runlength.txt', 'r');
huffman_table_white = cell(1, line_count);
index = cell(1, line_count);
for i = 1:line_count
    huffman_table_white(i) = {fscanf(fid, '%s', 1)};
    index(i) = {fscanf(fid, '%*s %s\n', 1)};
end
fclose(fid);

% same to black runlength code
fid = fopen('black_runlength.txt', 'r');
huffman_table_black = cell(1, line_count);
for i = 1:line_count
    huffman_table_black(i) = {fscanf(fid, '%s', 1)}; 
    index(i) = {fscanf(fid, '%*s %s\n', 1)};
end
fclose(fid);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% collect data from image to matrix

% read information in ccitt1_p1.pbm
 fid = fopen('ccitt1_p1.pbm','r');

% Alternatively read from other images

% fid = fopen('ccitt2_p1.pbm','r');
% fid = fopen('ccitt3_p1.pbm','r');
% fid = fopen('ccitt4_p1.pbm','r');
% fid = fopen('ccitt5_p1.pbm','r');
% fid = fopen('ccitt6_p1.pbm','r');
% fid = fopen('ccitt7_p1.pbm','r');
% fid = fopen('ccitt8_p1.pbm','r');

pattern = fgetl(fid);
comment = fgetl(fid);

% get rows and columns dimension
imgrows = fscanf(fid, '%d ',1);
imgcolumns = fscanf(fid, '%d ', 1);

% create matrix with binary codes ready for writing
[content_vector, count] = fscanf(fid, '%d ');
content_matrix = vec2mat(content_vector', imgcolumns);
fclose(fid);

% initial counter as 0
counter = 0;

% open ccitt1_p1_compress.pbm for compressing
fid=fopen('ccitt1_p1_compress.txt','w');

% alternatively, open others for compression
% fid=fopen('ccitt2_p1_compress.txt','w');
% fid=fopen('ccitt3_p1_compress.txt','w');
% fid=fopen('ccitt4_p1_compress.txt','w');
% fid=fopen('ccitt5_p1_compress.txt','w');
% fid=fopen('ccitt6_p1_compress.txt','w');
% fid=fopen('ccitt7_p1_compress.txt','w');
% fid=fopen('ccitt8_p1_compress.txt','w');

EOL = '000000000001';

% decide first digit of stream
if content_matrix(1,1) == 0
    flag = 'white';
else
    flag = 'black';
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% output compressing data to text document

% read 'imgrows' rows
for i = 1:imgrows
    current_line = content_matrix(i,:);
    if i > 1 
        if current_line == content_matrix(i - 1,:)
            % if line is the same as previous, output EOL
            fprintf(fid, EOL);
            continue;
        end
    end
    % read 'imgcolumns' columns
    for j = 1:imgcolumns
        % cosecutive black or white will increment counter
        if (current_line(j) == 0 && strcmp('white', flag)) || (current_line(j) == 1 && strcmp('black', flag))
            counter = counter + 1;
        else
            % for different flag will generate code and reload counter as 0
            if current_line(j) == 1 && strcmp('white', flag)
                output = huffman_table_CCITT_group3(counter, huffman_table_white, index);
                flag = 'black';
                fprintf(fid, output);
            elseif current_line(j) == 0 && strcmp('black', flag)
                output = huffman_table_CCITT_group3(counter, huffman_table_black, index);
                flag = 'white';
                fprintf(fid, output);
            end
            counter = 0;
        end
    end
    % every finished line will clean up counter and output its huffman code
    % according to flag is whether 'white' or 'black'
    if counter > 0
        if strcmp('white', flag)
            fprintf(fid, huffman_table_CCITT_group3(counter, huffman_table_white, index));
        else
            fprintf(fid, huffman_table_CCITT_group3(counter, huffman_table_black, index));
        end
        counter = 0;
    end
end
% close fileID
fclose(fid);

