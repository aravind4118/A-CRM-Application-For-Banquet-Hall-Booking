public class BillingTriggerHandlerClass {
    Public Static Void BillingCreationonBooking(List<Banquet_Hall__c> bHallList){
        List<Billing__c> billList = new List<Billing__c>();
        
        for(Banquet_Hall__c bHall : bHallList){
            Billing__c bil = new Billing__c();
            bil.Customer_Name__c =bHall.Id;
            bil.Email__c = bHall.Email__c;
            billList.add(bil);
        }
        if(!billList.isEmpty()){
            insert billList;
        }
        
    } 
}
