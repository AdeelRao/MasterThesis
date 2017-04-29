%KEEP IN MIND
%All files of matlab and python need to be run parallel
%should be in same workspace of matlab on left side
%try to put your python file also in designated path of matlab

clear all;
clc;
pathIn='C:\Users\Adeel\Desktop\Fungus\Check\lp114.jpg';
pathnew = 'C:\Users\Adeel\Desktop\Fungus\CheckN\';
% files=dir([pathIn '\*.jpg']);
a = imread(pathIn);
k = 1
% 

imwrite(a, fullfile(pathnew, 'File.jpg'))


afr = system('python filefrommatlab.py ')
if afr == 0
b = load('ab.mat')

z = b.ab
end
% b = imwrite(a,[pathnew,num2str(k),'.jpg'])

