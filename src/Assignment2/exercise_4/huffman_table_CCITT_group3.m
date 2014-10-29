function output = huffman_table_CCITT_group3(counter, huffman_table, index)

makeup_code = huffman_table(find(ismember(index, num2str(fix(counter / 64) * 64))));
terminating_code = huffman_table(find(ismember(index, num2str(rem(counter, 64)))));

if counter < 64
    output = char(terminating_code);
else
    output = char(strcat(makeup_code, terminating_code));
end
