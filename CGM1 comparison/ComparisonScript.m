Filein = readtable('HF059A08.csv');
Subject = 'HF059';
[m,n] = size(Filein);

%Pelvis Data search
for n = 1:n
    if Filein(0,n) == 'HF059:LPelvisAngles'
        Pelvisdata = Filein(2: ;n:n+3);
    end
end


        