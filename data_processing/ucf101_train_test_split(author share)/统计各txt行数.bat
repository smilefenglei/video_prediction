@echo off
setlocal enabledelayedexpansion
(for /f "delims=" %%a in ('dir /a-d /b *.txt') do (
set n=0
for /f "delims=" %%b in ('type "%%a"') do set /a n+=1
if "%%a" neq "统计.txt" echo,%%a --- !n!
))>"统计各txt行数.txt"