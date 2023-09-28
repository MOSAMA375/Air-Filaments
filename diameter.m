V=readmatrix('droplets');
Dn=V;
%delta=(L/(2^12))*10^6; %minimum cell size
histogram(Dn,BinWidth=0.2);
xlim([0 2.5]);
hold on
%line([delta, delta],ylim,'LineWidth',0.5,'color','red');
hold off
xlabel('d/D_o', 'FontName', 'Times-New-Roman', 'FontSize', 18 );
ylabel('counts' , 'FontName', 'Times-New-Roman', 'FontSize', 18);





