V=readmatrix('droplets'); %read file
Dn=V; 
%m=mean((Dn)); %mean
%s=std((Dn)); %standard deviation
%x=linspace(min(Dn),max(Dn),1000);
%pdf=(1./(x.*s*sqrt(2*pi))).*exp(-(log(x)-m).^2/(2*s^2)); %lognormal 
params=gamfit(Dn);
k=params(1);
theta=params(2);
x=0:0.1:max(Dn);
pdf = gampdf(x,k,theta);
plot(x,pdf,'LineWidth',2,Color='r') %pdf plot
xlim([0 2.5]);
fprintf('Shape (k): %.4f\n', k);
fprintf('Scale (theta): %.4f\n', theta);
hold on
histogram(Dn,NumBins=12,Normalization="pdf"); %histogram plot
hold on
xlabel('d/D_o', 'FontName', 'Times-New-Roman', 'FontSize', 18 );
ylabel('PDF' , 'FontName', 'Times-New-Roman', 'FontSize', 18);
