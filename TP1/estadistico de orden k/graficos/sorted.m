clear all
close all
Hf = figure(1)

set(Hf,'PaperUnits','inches','PaperPosition',[0 0 3.5 2.5])

Ha = axes

set(Ha,'Box','on','FontName','Arial','FontSize',8,'GridLineStyle','--','LineWidth',1,'TickDir','in');
grid on
hold on

SIM = dlmread("datos/fuerza_bruta.txt","\t",1,0)

plot(Ha,SIM(:,1),SIM(:,2),'-bo','linewidth',3,'markersize',4,'markerfacecolor','b');
plot(Ha,SIM(:,1),SIM(:,3),'-ro','linewidth',2,'markersize',3,'markerfacecolor','r');
plot(Ha,SIM(:,1),SIM(:,4),'-go','linewidth',1,'markersize',2,'markerfacecolor','g');

%axis([0 100000 0 650]);

ylabel('Tiempo [s]');
xlabel('Cantidad de elemento [n]');

Hleg = legend(Ha,'Estadistico orden k ,k = 0','Estadistico orden k ,k = n/2','Estadistico orden k ,k = n',"location",'northwest');
legend('boxoff');
set(Hleg,'FontName','Arial','FontSize',8);

print('fuerza bruta.png','-dpng','-r300');

return

