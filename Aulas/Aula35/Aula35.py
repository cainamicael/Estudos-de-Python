import datetime

data = datetime.datetime.now()
nasc = datetime.datetime(1978, 3, 7)

print(str(data.day) + '/' + str(data.month) + '/' + str(data.year))
print(nasc.strftime('%A'))#O dia da semana que foi essa data
"""
%a : txt dia da semana abreviado
%A : txt dia da semana completo
%w : Nº do dia da semana (Dom: 0, seg: 1 ...)
%W : Nº da semana do ano - semana 30
%d : Nº dia do mes
%b : txt mes abreviado
%B : txt mes completo
%n : Nº do mes
%y : Ano com 2 digitos
%Y : Ano com 4 digitos
%H : hora com 2 digitos 00 - 23
%I : 00 - 12
%p : AM/PM
%M : Minutos
%S : Segundos
%f : Micro segundos
%j : Dia do ano 001-366

"""